import { Injectable } from '@angular/core';
import { Action } from 'redux';

@Injectable()
export class PartyActions {
  static readonly TEST_ACTION = 'TEST_ACTION';

  testAction() {
    return {
      type: PartyActions.TEST_ACTION,
    };
  }
}
