import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import { CONSTANTS } from '../constants';
import { Party } from '../models/party.model';

@Injectable()
export class PartyService {
  private headers = new Headers({'Content-Type': 'application/json'});

  constructor(private http: Http) { }

  getUpcomingParty(): Promise<Party> {
    const url = `${CONSTANTS.API_URL}/parties/latest/`;
    return this.http.get(url)
     .toPromise()
     .then(response => {
       return response.json() as Party
      })
     .catch(error => {
       console.log('Error:', error);
     });
  }

}
