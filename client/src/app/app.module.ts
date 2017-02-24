import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { ViewsModule } from './views/views.module';
import { ComponentsModule } from './components/components.module';
import { UsersModule } from './users/users.module';
import { PartyModule } from './party/party.module';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,
    ViewsModule,
    ComponentsModule,
    UsersModule,
    PartyModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
