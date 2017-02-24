/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { PartyService } from './party.service';

describe('PartyService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PartyService]
    });
  });

  it('should ...', inject([PartyService], (service: PartyService) => {
    expect(service).toBeTruthy();
  }));
});
