# Useragent-parser-demo

Simple application that gets the user agent from anyone who access the app and count how many of each OS and how many of each browser have accessed the app.


# Usage

**To start the app in dev mode just:**

```
  ./scripts/devenv dev
```

**App deploy:**

 TO BE DONE
 
**To simple build the app:**
 
```
  ./scripts/devenv build
```   


**To scale the app:**

  Set the number of queues to create in the message broker through the variable `SCALE` in `docker-compose.yml` file. Its advisable to use the same numeber in all the services.
  Then use the command:
  
```
  ./scripts/devenv start
```

  and
  
```
  ./scripts/devenv scale <number-of-workers>
```
  
  
