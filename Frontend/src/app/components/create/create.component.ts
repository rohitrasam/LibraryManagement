import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Book } from 'src/app/core/models/book';
import { BookService } from 'src/app/core/services/book.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {

  isEdit!: boolean
  book!: Book
  bookId!: number


  updateForm!: FormGroup

  constructor(
    private activeRoute: ActivatedRoute,
    private bookService: BookService,
    private formBuilder: FormBuilder,
    private route: Router
  ) { }

  populateField(){
    this.updateForm.patchValue({
      name: this.book?.name,
      description: this.book?.description,
      price: this.book?.price,
      author: this.book?.author,
      quantity: this.book?.quantity,
      image: this.book?.image,
    })

  }

  ngOnInit(): void {
    this.checkEditMode()  
    if (this.isEdit) {
      this.getBookDetails()
    }

      this.updateForm = this.formBuilder.group({
          name: ["", Validators.required],
         description: ["", Validators.required],
          price: ["", Validators.required],
          author: ["", Validators.required],
          quantity: ["", Validators.required],
          image: ["", Validators.required]
        }) 
  }

  checkEditMode() {
    if(this.route.url === '/create'){
      this.isEdit = false
    }
    else{
      this.isEdit = true
    }
  }
 

  onSubmit() {
    if(this.isEdit) {
      this.book.name = this.updateForm.value.name
      this.book.description = this.updateForm.value.description
      this.book.price = this.updateForm.value.price
      this.book.author = this.updateForm.value.author
      this.book.quantity = this.updateForm.value.quantity
      this.book.image = this.updateForm.value.image
      this.bookService.updateBook(this.book).subscribe(data => {
        alert(data)
        this.goToDashboard()
      }, err => {
        alert(err.error)
      })
    }
    else if(!this.isEdit){
      
      const book = new Book()
      book.name = this.updateForm.value.name
      book.description = this.updateForm.value.description
      book.price = this.updateForm.value.price
      book.author = this.updateForm.value.author
      book.quantity = this.updateForm.value.quantity
      book.image = this.updateForm.value.image

      this.bookService.addBook(book).subscribe(data => {
        alert(data)
        this.route.navigate(['dashboard'])
      }, err => {
        alert(err.error)
      })
    }
  }

  getBookDetails(){
    this.activeRoute.queryParams.subscribe(params => {
      this.bookId = params['id']
    })
    this.bookService.getBook(this.bookId).subscribe(data => {
      this.book = data;
      
      this.populateField()
    })
  }

  goToDashboard() {
      this.route.navigate(['dashboard'])
  }
}
