import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PartyService } from './party.service';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [],
  providers: [PartyService],
})
export class PartyModule { }
