import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PartyService } from './party.service';
import { PartyActions } from './party.actions';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [],
  providers: [PartyService, PartyActions],
})
export class PartyModule { }
