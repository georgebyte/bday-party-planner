import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardViewComponent } from './views/dashboard/dashboard-view.component';
import { UsersViewComponent } from './views/users/users-view.component';
import { UserDetailsViewComponent } from './views/user-details/user-details-view.component';
import { GiftIdeasViewComponent } from './views/gift-ideas/gift-ideas-view.component';
import { CreatePartyViewComponent } from './views/create-party/create-party-view.component';
import { FundViewComponent } from './views/fund/fund-view.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard',  component: DashboardViewComponent },
  { path: 'users',  component: UsersViewComponent },
  { path: 'user/:id',  component: UserDetailsViewComponent },
  { path: 'ideas',  component: GiftIdeasViewComponent },
  { path: 'create-party',  component: CreatePartyViewComponent },
  { path: 'fund',  component: FundViewComponent },
];
@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
