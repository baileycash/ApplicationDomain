import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [UserService],
})
export class RegisterComponent implements OnInit {
  registerData;

  constructor(private userService: UserService) { }

  ngOnInit(){
    this.registerData = {
      username: '',
      email: '',
      password: ''
    };

  }

  registerUser(){
    this.userService.registerNewUser(this.registerData).subscribe(
      response => {
        alert(this.registerData.username + 'has been created!'), console.log(response);
      },
      error => console.log('Error', error)
    );
  }
}
