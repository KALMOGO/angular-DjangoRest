import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialsModule } from './modules/materials.module';
import { AppRoutingModule } from './app-routing';
import { ExercicesComponent } from './components/exercices/exercices.component';
import { MissionsComponent } from './components/missions/missions.component';
import { ProgrammerComponent } from './components/missions/programmer/programmer.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ExercicesComponent,
    MissionsComponent,
    ProgrammerComponent
  ],
  schemas:[CUSTOM_ELEMENTS_SCHEMA],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MaterialsModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
