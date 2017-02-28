import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { NgRedux } from '@angular-redux/store';
import { Observable } from 'rxjs/Observable';

import { Party } from '../../models/party.model';
import { PartyActions } from '../../party/party.actions';
import { Role } from '../../models/role.model';

@Component({
  selector: 'bpp-upcoming-party',
  templateUrl: './upcoming-party.component.html',
  styleUrls: ['./upcoming-party.component.css']
})
export class UpcomingPartyComponent implements OnInit, OnChanges {
  private userRole: Role;
  private mockedParty: any;

  @Input()
  party: Party;

  constructor(private ngRedux: NgRedux<any>) {
    ngRedux.select(['party']).subscribe(party => {
      this.mockedParty = party;
    });
  }

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

  onClick() {
    this.ngRedux.dispatch({type: PartyActions.TEST_ACTION});
  }

}
