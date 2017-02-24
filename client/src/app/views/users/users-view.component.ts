import { Component, OnInit } from '@angular/core';

import { User } from '../../models/user.model';
import { UsersService } from '../../users/users.service';

@Component({
  selector: 'bpp-users-view',
  templateUrl: './users-view.component.html',
  styleUrls: ['./users-view.component.css']
})
export class UsersViewComponent implements OnInit {
  private users: User[];

  constructor(private usersService: UsersService) { }

  ngOnInit() {
    this.usersService.getUsers().then(users => this.users = users);
  }

}
