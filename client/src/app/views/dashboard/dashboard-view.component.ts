import { Component, OnInit } from '@angular/core';

import { User } from '../../models/user.model';
import { Party } from '../../models/party.model';

import { UsersService } from '../../users/users.service';
import { PartyService } from '../../party/party.service';

@Component({
  selector: 'bpp-dashboard-view',
  templateUrl: './dashboard-view.component.html',
  styleUrls: ['./dashboard-view.component.css']
})
export class DashboardViewComponent implements OnInit {
  private nextPeopleToCelebrate: User[];
  private upcomingParty: Party;

  constructor(private usersService: UsersService, private partyService: PartyService) { }

  ngOnInit() {
    this.usersService.getUsers().then((users) => this.setNextPeopleToCelebrate(users));
    this.partyService.getUpcomingParty().then((party) => this.setUpcomingParty(party));
  }

  setNextPeopleToCelebrate(users: User[]): void {
    this.nextPeopleToCelebrate = users;
  }

  setUpcomingParty(party: Party): void {
    this.upcomingParty = party;
  }

}
