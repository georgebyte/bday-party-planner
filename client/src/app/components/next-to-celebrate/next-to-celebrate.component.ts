import { Component, Input, OnInit } from '@angular/core';

import { User } from '../../models/user.model';

@Component({
  selector: 'bpp-next-to-celebrate',
  templateUrl: './next-to-celebrate.component.html',
  styleUrls: ['./next-to-celebrate.component.css']
})
export class NextToCelebrateComponent implements OnInit {
  @Input()
  people: User[];

  constructor() { }

  ngOnInit() { }

}
