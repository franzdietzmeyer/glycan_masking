
# GLYCAN MASKING WORKFLOW

With this pipeline you should be able to perfom glycan masking in vaccine development using rosetta suite.



## Authors

- [@fradie21](https://github.com/fradie21/)




## Workflow

```

   ___ _                     __  __         _   _           
  / __| |_  _ __ __ _ _ _   |  \/  |__ _ __| |_(_)_ _  __ _ 
 | (_ | | || / _/ _` | ' \  | |\/| / _` (_-< / / | ' \/ _` |
  \___|_|\_, \__\__,_|_||_| |_|  |_\__,_/__/_\_\_|_||_\__, |
         |__/                                         |___/ 

    ┌───────────────┐                             
    │ prepare input │                             
    │      pdb      │                             
    └───────┬───────┘                             
            │                                     
            │                                     
 ┌──────────▼──────────┐                          
 │ CreateSequenceMotif │◄──────┐                  
 └──────────┬──────────┘       │                  
            │                  │                  
            │                  │                  
            │                  │                  
┌───────────▼───────────┐      │                  
│ FastRelax & Filtering │      │                  
└───────────┬───────────┘      │ ┌───────────────┐
            │                  │ │use FNxT motifs│
            │                  │ └───────────────┘
   ┌────────▼────────┐         │                  
   │  PTM Prediction │         │                  
   └────────┬────────┘         │                  
            │                  │                  
       ┌────▼────┐             │                  
       │Filtering├─────────────┘                  
       └────┬────┘                                
            │                                     
            │                                     
      ┌─────▼─────┐                               
      │Glycosylate│                               
      └─────┬─────┘                               
            │                                     
     ┌──────▼──────┐                              
     │Model_Glycans│                              
     └──────┬──────┘                              
            │                                     
       ┌────▼────┐                                
       │FastRelax│                                
       └─────────┘                                
```


