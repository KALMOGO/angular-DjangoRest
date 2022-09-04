export interface IResults{
  id:number,
  date_exercice:Date,
  etat_exercice:Boolean
}

export interface IExercices {
  count:number,
  next:string,
  previous:string,
  results:IResults[]
}
