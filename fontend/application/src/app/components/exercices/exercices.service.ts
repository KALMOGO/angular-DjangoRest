import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IExercices } from './exercices';

@Injectable({
  providedIn: 'root'
})
export class ExercicesService {
  httpOptions = {}
  public token:any;
  readonly endpointListCreate = "http://127.0.0.1:8000/exercices/"

  constructor(private http:HttpClient) {
    this.token = localStorage.getItem("token")
    console.log(this.token)
    this.httpOptions = {
       headers: new HttpHeaders({
          'Content-Type': 'application/json',
          'Authorization': "WEND-PANGA " + this.token
        },) }}

  getListeExercices():Observable<IExercices>{
    return this.http.get<IExercices>(this.endpointListCreate, this.httpOptions);
  }

  putExercices():Observable<any[]>{
    return this.http.get<any[]>(this.endpointListCreate);
  }

  deleteExercices():Observable<any[]>{
    return this.http.get<any[]>(this.endpointListCreate);
  }


}
