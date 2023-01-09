var data_count = parseInt("{{users_list.count}}");
  for (let i = 1; i <= data_count; i++) {
  let sr_no = document.getElementById("sr_no"+i);
  let close_button = document.getElementById("close_button"+i);
  let deleting = document.getElementById("delete");
  let hidden_data = document.getElementById("panel"+i);
 let main_div = document.getElementById("clr"+i);
let data_heading = document.getElementById("heading_data");
 main_div.addEventListener("click",()=>{
if (sr_no.style.display !== "none"){
  
 sr_no.style.display = "none";
 hidden_data.classList.remove("panel_none");
 data_heading.innerHTML = "#MakeChanges";
 
}

else{
sr_no.style.display = "block";
hidden_data.classList.add("panel_none");
data_heading.innerHTML="#";}

 });

}