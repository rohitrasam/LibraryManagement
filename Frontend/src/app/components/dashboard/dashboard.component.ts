import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Book } from 'src/app/core/models/book';
import { AuthService } from 'src/app/core/services/auth.service';
import { BookService } from 'src/app/core/services/book.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  name!: string | null
  books!: Book[]
  constructor(
    private authService: AuthService, 
    private bookService: BookService, 
    private route: Router,
    ) { }

  ngOnInit(): void {
    this.getUsername()
    this.getBooks()
  }

  getUsername(){
    this.name = localStorage.getItem('name')
  }

  getBooks(){
    this.bookService.getBooks().subscribe(data => {
      this.books = data 
   })
  }
  
  gotoCreate(){
    this.route.navigate(['create'])
  }

  gotoUpdate(id: number){
    this.route.navigate(['edit'], {queryParams: {id: id}})
  }

  deleteBook(id: number){
    this.bookService.deleteBook(id).subscribe(data => {
      alert(data)
    })
  }

  logout() {
    this.authService.logout()
  }
}
