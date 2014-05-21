
var showConfirmation = false;

 $(document).ready(function () {
     $('#field-description').keyup(function () {
         var input = $(this).val();
         if (this.defaultValue != input){
             showConfirmation = true;
         }
         else{
             showConfirmation = false;
         }
     });
     $("input[type='submit']").click(function(){
         showConfirmation = false;
     })
 });

 function confirmExit() {
     if (showConfirmation) {
         return("You typed something in the textbox.");
     }
 }

 window.onbeforeunload = confirmExit;