import pandas as pd

profile_FunnyCar = pd.DataFrame(
    {"Name": ["Matt Hagan", "Tommy Johnson Jr", "Jack Beckman", "Ron Capps", "Bob Tasca III", 
             "J.R. Todd", "Tim Wilkerson", "Alexis DeJoria", "Paul Lee", "Cruz Pedgregon",
             "Blake Alexander", "Jim Campbell", "Terry Haddock", "Bob Bode", "Dale Creasy Jr", 
             "John Force", "Dave Richards", "Alex Miladinovich", "Robert Height", "Jeff Arend", 
             "Mike McIntire Jr", "Chad Green", "Jeff Diehl", "Mike Smith", "John Smith", "John Hale", 
             "Gary Densham", "Frank Pedregon", "Tim Gibbons", "Chris Morel", "Johnnie Lindberg"],
     
     "DOB": ["11/18/1982", "4/6/1968", "6/28/1966", "6/20/1965", "10/14/1975", 
             "12/16/1981", "12/29/1960", "9/24/1977", "9/16/1957", "9/19/1963",
             "9/26/1988", "12/29/1962", "12/15/1970", "9/7/1951", "7/31/1959", 
             "5/4/1949", "6/13/1978", "8/20/1976", "8/20/1969", "11/27/1962", 
             "8/21/1984", "5/15/1973", "7/27/1964", "8/18/1965", "1/30/1967", "4/19/1965", 
             "10/20/1946", "", "7/22/1965", "10/29/1976", "9/1/1989"], 
     
     "Residence_City": ["Christiansburg", "Avon", "Narco", "Carlsbad", "Hope", 
             "Jupiter", "Springfield", "Austina", "Orange", "Brownsburg",
             "Charlotte", "Huntington Beach", "Temple", "Barrington", "Bleecher", 
             "Yorba Linda", "Wellington", "Orange", "Yorba Linda", "La Verne", 
             "Chesterland", "", "Monterey", "Lake Worth", "", "Addison", 
             "Bellflower", "Gardena", "Redding", "Reno", "Brownsburg"], 
     
     "Residence_State": ["Virginia", "Indiana", "California", "California", "Rhode Island", 
             "Florida", "Illinois", "Texas", "California", "Indiana",
             "North Carolina", "California", "Texas", "Illinois", "Illinois", 
             "California", "Florida", "California", "California", "California", 
             "Ohio", "", "California", "Florida", "", "Texas", 
             "California", "California", "California", "Nevada", "Indiana"], 
    
     "Sponsor": ["Mopar/Pennzoil/Sandvik Dodge Charger SRT Hellcat", "MD Anderson Cancer Center Dodge Charger SRT Hellcat",
            "Infinite Hero Foundation Dodge Charger SRT Hellcat", "NAPA Auto Parts Dodge Charger SRT Hellcat",
            "Ford Motorcraft/Quick Lane Mustang", "DHL Toyota Camry", "Levi, Ray & Shoup Ford Shelby Mustang",
            "ROKiT/ABK Beer Toyota Camry", "McLeod Racing/FTI Performance Charger", "Snap-on Tools Dodge Charger SRT Hellcat",
             "Head Inc./Pronto Auto Parts Ford Mustang", "DiPinto International Logistics Dodge Charger", "ChecklistBoards.com Mustang", "Bode Motorsports Toyota", "Tek-Pak Chevrolet Camaro", 
             "PEAK Chevrolet Camaro SS", "Paul Richards Racing/Prestige Ford Mustang", "Hot For Teacher Toyota", "Auto Club Chevrolet Camaro SS", "", 
             "McAttack Racing Toyota Camry", "", "Jeff Diehl Racing Toyota Solara", "", "Rock Batteries Dodge Charger", "", 
             "Densham Motorsports Mustang", "", "Castle Rock Trucks/Race One Media Charger", "", "Halvotech"],

       "Crew Chief": ["Dickie Venables", "John Collins", "Dean Antonelli", "John Medlen", "Mike Neff/Jon Schaeffer", 
             "Jon Oberhofer/Todd SMith", "Tim Wilkerson/Richard Hartman", "Del Worsham/Nicky Bonifante", 
               "Jim Oberhofer", "John Collins/Rip Reynolds",
             "Jim Head", "Jim Dunn", "Terry Haddock", "John Stewart", "Dale Creasy Jr", 
             "Danny Hood", "Paul Smith", "Kevin Poynter", "Jimmy Prock/Chris Cunningham",
            "Dean Marinis", "Tony Shortall", "Chad Green", "Aaron Brooks", 
               "Mike Smith", "Paul Smith", "Del Worsham", 
             "Gary Densham", "Chuck Worsham", "Tim Gibbons", "Terry Manzer", 
               "Johnnie Lindberg"],
     
   "Career Wins": ["39", "24", "34", "68", "11",  "19", "23", "8", "3", "42",
             "2", "0", "0", "1", "0", "154", "0", "0", "53", "4", 
             "0", "1", "0", "0", "0", "0", 
             "8", "4", "0", "0", "8"] ,
 
     "Career Final Rounds": ["71", "62", "72", "131", "29", "40", "50", "15", "4", "86",
             "4", "0", "0", "1", "0",  "261", "0", "0", "85", "9", 
             "0", "3", "0", "0", "0", "1", 
             "21", "9", "0", "0", "14"],   

     "Career Best ET": ["3.799", "3.837", "3.825", "3.837", "3.851",  "3.856", "3.844", "3.863", "3.882", "3.886",
             "3.921", "3.977", "4.08", "4.027", "4.037", "3.832", "3.975", "4.554", "3.793", "3.93", 
             "3.977", "3.998", "4.021", "4.192", "4.082", "3.956", 
             "3.938", "", "4.517", "4.18", "3.865"],  
 
     "Career Best Speed": ["338.85", "332.02", "335.57", "339.28", "335", "334.3", "333.74", "333.16", "332.92", "332.25",
             "325.22", "318.77", "300", "317.05", "306.46", 
             "337.16", "316.60", "246.71", "339.87", "323.97", 
             "309.49", "310.70", "316.45", "297.75", "307.23", "319.75", 
             "318.36", "", "275.84", "290", "331.53"]  
  
    
    }
     )
profile_FunnyCar