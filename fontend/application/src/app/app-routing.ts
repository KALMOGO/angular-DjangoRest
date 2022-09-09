import {  NgModule } from "@angular/core";
import { RouterModule,Routes } from "@angular/router";
import { ExercicesComponent } from "./components/exercices/exercices.component";
import { LoginComponent } from "./components/login/login.component";
import { MissionsComponent } from "./components/missions/missions.component";
import { OrdreMissionComponent } from "./components/missions/ordre-mission/ordre-mission.component";

const router :Routes = [
  {path:'', component: LoginComponent },
  {path:'exercices', component: ExercicesComponent },
  {path:'missions', component:MissionsComponent},
  {path:'ordre', component:OrdreMissionComponent}
]

@NgModule({
   imports:[RouterModule.forRoot(router)],
   exports:[RouterModule]
})

export class AppRoutingModule{}
