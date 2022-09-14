import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { User } from '../models/user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private url = environment.base_url
  constructor(private http: HttpClient) { }

  userLogin(data: {email: string, password: string}): Observable<User> {
      return this.http.post<User>(`${this.url}login/`, data)
  }

  createUser(user: User): Observable<string>{
    return this.http.post<string>(`${this.url}signup/`, user)
  }
}
