import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Book } from '../models/book';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  private url = environment.base_url
  constructor(private http: HttpClient) { }

  getBooks(): Observable<Book[]>{
    return this.http.get<Book[]>(`${this.url}get_books/`)
  }

  addBook(book: Book): Observable<string>{
    return this.http.post<string>(`${this.url}add_book/`, book)
  }

  getBook(id: number): Observable<Book>{
    return this.http.get<Book>(`${this.url}get_book/${id}`)
  }

  updateBook(book: Book): Observable<string>{
    return this.http.patch<string>(`${this.url}update_book/${book.id}`, book)
  }

  deleteBook(id: number): Observable<string>{
    return this.http.delete<string>(`${this.url}delete_book/${id}`)
  }
}
