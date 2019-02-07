import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  API_URL = 'http://127.0.0.1:8000/api/'

  constructor(private http: HttpClient) { }

  getUserDetails(username, password) {

  }

  registerNewUser(userData): Observable<any> {
    return this.http.post('http://127.0.0.1:8000/api/users/', userData)
  }

}
