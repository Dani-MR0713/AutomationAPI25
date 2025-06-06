# First Task - CURL request
#### Jira REST API by Daniela Marañon

**Pre-condition** 
1. Set the User and ApiToken
> export apiToken=ATATT3xFfGF0hUW6aFjgCQAWS_Ooad-oh1MpA3yE6zSYDQj7gSl0g6-oBmyN76IAL8GDb8nGVfgMB7Rpy73_fKKoP-pN0VICaLzJVWehFl19GGArrfAc9dA_jF-aNr8tACZROIlWQDIMMsi8pNANFEBg0OizzWLiOxlP6EYQolZmPxLD5hrfXZw=25E583F7
>
> echo $apiToken
> 
> export user=daniela.maranon.jalasoft@gmail.com
>
> echo $user

2. Import a data processor in JSON format (jq) through Chocolatey (package manager for Windows)
> choco install jq

3. Create your own Jira instance and API token.
   * Instance
![image](https://github.com/user-attachments/assets/b1250de3-6f1e-42bf-ac49-dc0039232ca2)
   * API Token
![image](https://github.com/user-attachments/assets/b55e8ed1-dbd6-4f31-9543-7bec9295891c)


### **GET**

GET an **Issue** by ID.

```shell
curl -u $user:$apiToken -X GET -H "Content-Type: application/json" https://dmaranon.atlassian.net//rest/api/3/issue/10040 | jq
```
output to file
```shell
curl -u $user:$apiToken -X GET -H "Content-Type: application/json" https://dmaranon.atlassian.net//rest/api/3/issue/10040 -o output2.json | jq
```
See the details of the response
```shell
curl -u $user:$apiToken -X GET -H "Content-Type: application/json" https://dmaranon.atlassian.net//rest/api/3/issue/10040 -v | jq
```

### **POST**

Create a new **Issue**.
```shell
curl -u $user:$apiToken -X POST -H "Content-Type: application/json" --data '{
  "fields": {
    "issuetype": {
      "id": 10007
    },
    "project": {
      "id": "10001"
    },
    "summary": "Nuevo 10"
  }
}' -H "Content-Type: application/json" https://dmaranon.atlassian.net/rest/api/3/issue
```

### **PUT**

Update the Summary field of the **Issue**.
```shell
curl -u $user:$apiToken -X PUT --data '{
  "fields": {
    "summary": "UPDATED"
  }
}' -H "Content-Type: application/json" https://dmaranon.atlassian.net/rest/api/3/issue/MPDD-10
```

### **DELETE**

Delete an **Issue** by ID.

```shell
curl -u $user:$apiToken -X DELETE -H "Content-Type: application/json" https://your-domain.atlassian.net/rest/api/3/issue/MPDD-10?deleteSubtasks=true
```

### **NEGATIVE CASES**
1. Create an issue without mandatory fields.

```shell
 curl -u $user:$apiToken -X POST --data '{
     "fields": {
         "summary": "Issue sin campos obligatorios"
     }
 }' -H "Content-Type: application/json" https://dmaranon.atlassian.net/rest/api/3/issue/ | jq
```
**Response:**

![image](https://github.com/user-attachments/assets/2b07a8c2-c63e-4a77-8035-2c2b17421050)

2. Get a non-existent issue. 
```shell
curl -u $user:$apiToken -X GET -H "Content-Type: application/json" https://dmaranon.atlassian.net//rest/api/3/issue/10050 | jq
```
**Response:**

![image](https://github.com/user-attachments/assets/66d4333e-acfd-477e-a703-3699f2d7f498)

3. Update an issue with a field not allowed.
```shell
curl -u $user:$apiToken -X PUT --data '{
  "fields": {
    "nonexistentField": "Valor no permitido"
  }
}' -H "Content-Type: application/json" https://dmaranon.atlassian.net/rest/api/3/issue/MPDD-10 | jq
```
**Response:**

![image](https://github.com/user-attachments/assets/e55ecaf3-409e-46e5-b90b-cf2a3d1c2a02)


4.  Delete an issue without permissions
```shell
curl -u $unauthorizedUser:$apiToken -X DELETE -H "Content-Type: application/json" https://your-domain.atlassian.net/rest/api/3/issue/MPDD-11?deleteSubtasks=true | jq
```
**Response:**

![image](https://github.com/user-attachments/assets/2847fb9b-81b1-4987-8e88-b875cbef4576)
