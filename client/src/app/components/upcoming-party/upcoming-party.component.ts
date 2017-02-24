import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';

import { Party } from '../../models/party.model';
import { Role } from '../../models/role.model';

@Component({
  selector: 'bpp-upcoming-party',
  templateUrl: './upcoming-party.component.html',
  styleUrls: ['./upcoming-party.component.css']
})
export class UpcomingPartyComponent implements OnInit, OnChanges {
  private userRole: Role;

  @Input()
  party: Party;

  constructor() { }

  ngOnInit() {

  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['party'] && changes['party']['users']) {
      this.findAndSetUserRole(changes['party']['users']);
    }
  }

  findAndSetUserRole(users) {
    console.log('users', users);
  }

}
