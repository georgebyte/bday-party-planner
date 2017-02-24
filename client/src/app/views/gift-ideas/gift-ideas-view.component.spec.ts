/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { GiftIdeasViewComponent } from './gift-ideas-view.component';

describe('GiftIdeasViewComponent', () => {
  let component: GiftIdeasViewComponent;
  let fixture: ComponentFixture<GiftIdeasViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GiftIdeasViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GiftIdeasViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
