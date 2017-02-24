import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { MainNavigationComponent } from './main-navigation/main-navigation.component';
import { FooterComponent } from './footer/footer.component';
import { UpcomingPartyComponent } from './upcoming-party/upcoming-party.component';
import { NextToCelebrateComponent } from './next-to-celebrate/next-to-celebrate.component';
import { UsersListComponent } from './users-list/users-list.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  exports: [
    HeaderComponent,
    MainNavigationComponent,
    FooterComponent,
    UpcomingPartyComponent,
    NextToCelebrateComponent,
    UsersListComponent
  ],
  declarations: [
    HeaderComponent,
    MainNavigationComponent,
    FooterComponent,
    UpcomingPartyComponent,
    NextToCelebrateComponent,
    UsersListComponent
   ],
})
export class ComponentsModule { }
