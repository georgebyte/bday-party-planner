import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { MainNavigationComponent } from './main-navigation/main-navigation.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [
    HeaderComponent,
    MainNavigationComponent,
    FooterComponent
  ],
  declarations: [
    HeaderComponent,
    MainNavigationComponent,
    FooterComponent
   ],
})
export class ComponentsModule { }
