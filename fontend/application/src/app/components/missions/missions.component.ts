import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { map, Observable, Subscription } from 'rxjs';

@Component({
  selector: 'app-missions',
  templateUrl: './missions.component.html',
  styleUrls: ['./missions.component.css']
})
export class MissionsComponent implements OnInit {
   sub:Subscription = new Subscription();
   exercice_id!:number; // exercice parent à la mission

   //ajout
  typesOfShoes: string[] = ['ouedradrogo Amado', 'Karim Is', 'Ms  salif', 'Moccasins', 'Sneakers'];

  menuMission:string[]=['Acceuil', 'Nouvelle mission']

  constructor(private route : ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    //ajout


    //good
   this.exercice_id = this.exercice_parent();
  }

  exercice_parent():number{
    // methode permettant de retourner l'exercice parent d'une mission
    let queryParam:any;

       this.route.queryParamMap  //Recuperation des parametres state d'url : ActivatedRoute
      .subscribe((params) => {
         queryParam = {...params }; // operateur de diffussion

       });
       return queryParam.params.exercice
  }

  gotoProgrammation(){
    this.router.navigate(['missions/programmation'],
    { queryParams: {'exercice':this.exercice_id}})
  }

  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
