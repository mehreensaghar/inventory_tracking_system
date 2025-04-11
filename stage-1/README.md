Stage 1:Single Store 

Objective:
.basic backend inventory system for a single kiryana store
.Track products and stock movements using local storage.

 Tech Used:
- Python
- SQLite 

Data Model

1)Product Table       

id      INT      Primary key           
name    TEXT     Product name          
sku     TEXT     Unique identifier     

2)StockMovement Table
id            INT        Primary key                           
product_id    INT        FK to Product                         
type          TEXT       stock_in, sale, manual_removal        
quantity      INT        Movement amount                       
timestamp     DATETIME   Auto-generated                       



