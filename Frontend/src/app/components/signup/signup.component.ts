import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { User } from 'src/app/core/models/user';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  isEdit!: boolean
  user!: User
  userSubscription!: Subscription

  updateForm!: FormGroup

  constructor(

    private userService: UserService,
    private formBuilder: FormBuilder,
    private route: Router
  ) { }


  ngOnInit(): void {
      this.updateForm = this.formBuilder.group({
          name: ["", Validators.required],
          email: ["", Validators.required],
          ph_no: ["", Validators.required],
          newPassword: ["", this.isEdit ? null : Validators.required ],
          confirmPassword: ["", this.isEdit ? null : Validators.required ]
        }) 
  }

  checkPassword = (password: string, confirmPassword: string) => password === confirmPassword 

  onSubmit() {
    const password = this.updateForm.value.newPassword
    const confirmPassword = this.updateForm.value.confirmPassword
    if(this.checkPassword(password, confirmPassword)){
      
      const user = new User()
      user.name = this.updateForm.value.name
      user.email = this.updateForm.value.email
      user.ph_no = this.updateForm.value.ph_no
      user.password = this.updateForm.value.newPassword
      user.isAdmin = this.updateForm.value.isAdmin

      this.userService.createUser(user).subscribe(data => {
        alert(data)
        this.route.navigate(['login'])
      }, err => {
        alert(err.error)
      })
    }
    else{
      alert("Passwords don't match")
    }
  }

  goToDashboard() {
    if(this.isEdit){
      this.route.navigate(['dashboard'])
    }
    else{
      this.route.navigate(['login'])
    }
  }

  ngOnDestroy(): void{
    if(this.isEdit) this.userSubscription.unsubscribe()
  }
}
