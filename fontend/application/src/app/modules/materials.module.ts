import { NgModule } from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import {MatCardModule} from '@angular/material/card';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatListModule} from '@angular/material/list';
import {ScrollingModule} from '@angular/cdk/scrolling';
import {MatDividerModule} from '@angular/material/divider';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import {MatSelectModule} from '@angular/material/select';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatRadioModule} from '@angular/material/radio';
import {MatIconModule} from '@angular/material/icon';
import {MatDialogModule} from '@angular/material/dialog';
import {MatSnackBarModule} from '@angular/material/snack-bar';

const materialComponents: any[] = [
     MatButtonModule,
     MatFormFieldModule,
     MatInputModule,
     MatCardModule,
     MatSidenavModule,
     MatGridListModule,
     MatListModule,
     ScrollingModule,
     MatDividerModule,
     MatAutocompleteModule,
     MatButtonToggleModule,
     MatDatepickerModule,
     MatNativeDateModule,
     MatSelectModule,
     MatCheckboxModule,
     MatRadioModule,
     MatIconModule,
     MatDialogModule,
     MatSnackBarModule,


]

@NgModule({
  declarations:[],
  exports: [materialComponents],
  imports: [materialComponents]
})

export class MaterialsModule { }
