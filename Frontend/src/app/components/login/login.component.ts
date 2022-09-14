import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { UserService } from 'src/app/core/services/user.service';
// import { faBank, faArrowRightToBracket, faIdCard, faEnvelope, faKey } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm!: FormGroup
  id!: Number

  constructor(
    private formBuilder: FormBuilder,
    private authService: AuthService,
    private route: Router,
    private loginService: UserService
    ) { }

  ngOnInit(): void {
    this.initialzeLogin()
    
  }

  initialzeLogin() {
    this.loginForm = this.formBuilder.group(
      {
        email: ['', Validators.required],
        password: ['', Validators.required]
      }
    )
  }


  goToRegister(){
    this.route.navigate(['signup'])
  }

  onSubmit(){
    const email = this.loginForm.value.email
    const password = this.loginForm.value.password
    this.loginService.userLogin({'email': email, 'password': password}).subscribe(data => {  
      localStorage.setItem('data', String(data.id))
      this.authService.setToken(""+Math.random() * 1000 + 987987)
      this.route.navigate(['dashboard'])
    }, err => {
        alert(err.error)
    })  
  }

}
