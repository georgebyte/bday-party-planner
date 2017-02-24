/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { NextToCelebrateComponent } from './next-to-celebrate.component';

describe('NextToCelebrateComponent', () => {
  let component: NextToCelebrateComponent;
  let fixture: ComponentFixture<NextToCelebrateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NextToCelebrateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NextToCelebrateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
