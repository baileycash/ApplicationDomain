import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private userService: UserService) { }

  ngOnInit() {
  }

  loginUser(event) {
    const target = event.target
    const username = target.querySelector('#username').value
    const password = target.querySelector('#password').value

    this.userService.getUserDetails(username, password)
  }

}
