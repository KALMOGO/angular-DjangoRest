import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenService } from './authen.service';

export interface Iuser{
  username : String,
  password:String,
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  httpOptions = {}

  userLoginForm = new FormGroup({
    username: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
  })

  invalid_Hint = false;
  constructor(
    private authService:AuthenService,
    private route:Router
    ){}

    ngOnInit() {
      this.logout()
    }

    // methode d'obtention du token (connexion)
    onLoginAction(userData: any) {

      const utilisateur = {
         'username': userData.username,
         'password': userData.password
        }

      this.authService.login(utilisateur);
      this.onConnected()
    }
   // ralentie pour attendre la reponse du backend: (ameliorable avec un subscribe)
    onConnected(){
      setTimeout(()=>{
        if (this.authService.isAuthenticated()){
          this.userLoginForm.reset()
          //this.authService.refreshToken()
          this.route.navigate(['exercices']) // navigation

        }else{
          this.invalid_Hint = true;
        }
      }, 1000)
    }

    // methodes de rafraichissement et de suppression (deconnexion) du token
    // refreshToken() {
    //   this.authService.refreshToken();
    // }

    logout() {
      this.authService.logout();
    }

    // necessaire pour tout attaque a la Bd
  //   this.httpOptions = {
  //     headers: new HttpHeaders({
  //    'Authorization': "WEND-PANGA" + this.authService.token
  //  })}
}
