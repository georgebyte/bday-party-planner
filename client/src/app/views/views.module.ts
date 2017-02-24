import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardViewComponent } from './dashboard/dashboard-view.component';
import { UsersViewComponent } from './users/users-view.component';
import { UserDetailsViewComponent } from './user-details/user-details-view.component';
import { GiftIdeasViewComponent } from './gift-ideas/gift-ideas-view.component';
import { CreatePartyViewComponent } from './create-party/create-party-view.component';
import { FundViewComponent } from './fund/fund-view.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    DashboardViewComponent,
    UsersViewComponent,
    UserDetailsViewComponent,
    GiftIdeasViewComponent,
    CreatePartyViewComponent,
    FundViewComponent
  ]
})
export class ViewsModule { }
