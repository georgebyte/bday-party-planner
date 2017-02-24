import { Component, Input, OnInit } from '@angular/core';

import { Party } from '../../models/party.model';
import { Role } from '../../models/role.model';

@Component({
  selector: 'bpp-upcoming-party',
  templateUrl: './upcoming-party.component.html',
  styleUrls: ['./upcoming-party.component.css']
})
export class UpcomingPartyComponent implements OnInit {
  private userRole: Role;

  @Input()
  party: Party;

  constructor() { }

  ngOnInit() {
    this.userRole = {
      name: 'Test role',
      description: 'Chill out!',
    }
  }

}
