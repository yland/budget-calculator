
    // getting data from server
    getData = function(){
      
        $('#inc-table td').empty();
        $('#exp-table td').empty();
        $('.saving strong').empty();
    
        $.ajax({
            type: 'GET',
            url: 'http://0.0.0.0:8000/get_result',
            contentType: "application/json",
            dataType: 'json',
            success: function (data) {
                console.log(data['saving']);
             $('.saving').append('<strong>'+data["saving"]+'</strong>')   
              var incomelist = data["income"];
              var expenselist = data["expense"];     
              
              for ( var i = 0, l = incomelist.length; i < l; i++ ) {
                  income = incomelist[ i ];
                  
                  for (let key in income){
                    $('#inc-table').append($(
                    $.map(income[key], function(amt, description){
                      return '<tr><td>'+description+'</td><td>'+amt+'</td><td><button type="button" <button onclick="delete_inc('+key+')" id="delete-inc">'+'Remove'+'</button></td></tr>'
    
                    }).join('')
                  ));
                  }
                }
    
                for ( var i = 0, l = expenselist.length; i < l; i++ ){ 
                  expense = expenselist[ i ]; 
                  for (let key in expense){      
                    $('#exp-table').append($(
                     $.map(expense[key], function(amt, description){
                      return '<tr><td>'+description+'</td><td>'+amt+'</td><td><button type="button" <button onclick="delete_exp('+key+')" id="delete-exp">'+'Remove'+'</button></td></tr>'
    
                      }).join('')
                    )); 
                  }
                
                }
            }//End Success function 
                
          });
        };
      getData();

          $('#add_income').on('click', function(){
                  $.ajax({ 
                  type: 'POST',
                  url: 'http://0.0.0.0:8000/add_income', 
                  contentType: "application/json",
                  dataType: "json",
                  data: JSON.stringify({
                      "inc": $('#inc_des').val(),
                      "amt": $('#inc_amt').val()
                  }),   
                  success: function(resp){
                  console.log('resp', resp)
                     getData(); 
                     
      
                  },
                  error: function(resp){
                    
                    alert("Error adding income!");
                  } 
                });   
           });
      
          $('#add_expense').on('click', function(){
              $.ajax({ 
              type: 'POST',
              url: 'http://0.0.0.0:8000/add_expense',
              contentType: "application/json",
              dataType: "json",
              data: JSON.stringify({
                  "exp": $('#exp_des').val(),
                  "amt": $('#exp_amt').val()
              }),   
      
              success: function(response){
                 
                  getData();
              },
              error: function(response){
                    
                    alert("Error posting expense!");
              }
              
              });
              
          });
      
      delete_inc = function (id) {
          
          jQuery.ajax({
            type: 'DELETE',
            url: 'http://0.0.0.0:8000/delete_income',
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({"key":id}),
            success: function(resp) {
                console.log('Income Deleted!')
                getData();
            }
          });
        }
      
      delete_exp = function (k) {
          
        jQuery.ajax({
          type: 'DELETE',
          url: 'http://0.0.0.0:8000/delete_expense',
          contentType: "application/json",
          dataType: "json",
          data: JSON.stringify({"key":k}),
          success: function(resp) {
              console.log('Expense deleted!')
              getData();
          }
        });
      }