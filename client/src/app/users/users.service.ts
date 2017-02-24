import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import { CONSTANTS } from '../constants';
import { User } from '../models/user.model';

@Injectable()
export class UsersService {
  private headers = new Headers({'Content-Type': 'application/json'});

  constructor(private http: Http) { }

  getUsers(): Promise<User[]> {
    const url = `${CONSTANTS.API_URL}/users/`;
    return this.http.get(url)
     .toPromise()
     .then(response => {
       return response.json().results as User[]
      })
     .catch(error => {
       console.log('Error:', error);
     });
  }

}
