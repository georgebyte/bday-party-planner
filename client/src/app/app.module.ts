import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgReduxModule, NgRedux, DevToolsExtension } from '@angular-redux/store';
import { NgReduxRouterModule, NgReduxRouter, routerReducer } from '@angular-redux/router';
import { provideReduxForms, composeReducers, defaultFormReducer } from '@angular-redux/form';

import { combineReducers } from 'redux';

import { ViewsModule } from './views/views.module';
import { ComponentsModule } from './components/components.module';
import { UsersModule } from './users/users.module';
import { PartyModule } from './party/party.module';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    NgReduxModule,
    NgReduxRouterModule,
    AppRoutingModule,
    ViewsModule,
    ComponentsModule,
    UsersModule,
    PartyModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(
    private ngRedux: NgRedux<any>, // TODO: Create interface representing state hierarchy
    devTools: DevToolsExtension,
    ngReduxRouter: NgReduxRouter
  ) {
    // Define the global store shape by combining our application's
    // reducers together into a given structure.
    const rootReducer = composeReducers(
      defaultFormReducer(),
      combineReducers({
        router: routerReducer,
      })
    );

    // Tell Redux about our reducers and epics. If the Redux DevTools
    // chrome extension is available in the browser, tell Redux about
    // it too.
    ngRedux.configureStore(
      rootReducer, // root reducer
      {}, // initial state
      [], // middleware
      devTools.isEnabled() ? [ devTools.enhancer() ] : [] // enhancers
    );

    // Enable syncing of Angular router state with our Redux store.
    ngReduxRouter.initialize();

    // Enable syncing of Angular form state with our Redux store.
    provideReduxForms(ngRedux);
  }
}
