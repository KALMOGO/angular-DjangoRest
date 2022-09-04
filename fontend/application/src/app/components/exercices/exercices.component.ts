import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { IExercices, IResults } from './exercices';
import { ExercicesService } from './exercices.service';

@Component({
  selector: 'app-exercices',
  templateUrl: './exercices.component.html',
  styleUrls: ['./exercices.component.css']
})
export class ExercicesComponent implements OnInit {

  listeExercices:IExercices[] = [];

  constructor(
    private exerciceSercice:ExercicesService,
    private router:Router) { }

  ngOnInit(): void {
    this.exerciceSercice.getListeExercices().subscribe(
      (value:IExercices)=>{
        this.listeExercices.push(value)
      },
      (err:any)=>{
        console.log(err)
      },
      ()=>{},
    )
  }

  loginMission(exercice:IResults){
    // transmission de parametre à une route sans specifier la params dans AppRouting
      this.router.navigate(
          ['missions'], { queryParams: {'exercice':exercice.id}});
  }

}
