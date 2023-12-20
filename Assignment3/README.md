# Assignment 3
```sh
func start

Found Python version 3.8.16 (python3).
Azure Functions Core Tools
Core Tools Version:       4.0.5441 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.25.3.21264
[2023-12-19T10:28:17.816Z] Worker process started and initialized.
Functions:
        Employee_ServiceBus: [GET,POST] http://localhost:7071/api/Employee_ServiceBus
        AddEmployeeDetails_ServiceBus: serviceBusTrigger
        DeleteEmployeeDetails_ServiceBus: serviceBusTrigger

For detailed output, run func with --verbose flag.
[2023-12-19T10:28:22.631Z] Host lock lease acquired by instance ID '0000000000000000000000007053F404'.
```

Initial employee_details.csv file
```csv
EmployeeID,Name,DOB,Position
3450,Foram Jivani,09/12/1991,MLE
3485,Abc XYC,01/01/1990,Sr MLE
3330,Def XYC,01/02/1996,Analyst
3200,ERF XYC,06/08/1992,MLE
2009,Abc XYC,01/01/1990,Sr MLE
2008,Def XYC,01/02/1996,Analyst
2001,ERF XYC,06/08/1992,MLE
2010,Abc XYC,01/01/1990,Sr MLE
1010,Def XYC,01/02/1996,Analyst
1100,ERF XYC,06/08/1992,MLE
5200,Abc XYC,01/01/1990,Sr MLE
2586,Def XYC,01/02/1996,Analyst
9874,ERF XYC,06/08/1992,MLE
1111,ERF XYC,06/08/1992,MLE
5598,Abc XYC,01/01/1990,Sr MLE
7845,Def XYC,01/02/1996,Analyst
9854,ERF XYC,06/08/1992,MLE
```

Send `POST` request to  
`http://localhost:7071/api/Employee_ServiceBus?Operation=AddEmployee`
with following json body
```
{
    "EmployeeID": 5555,
    "Name": "Dimple Jain",
    "DOB": "15/08/1996",
    "Position": "Analyst"
}
```

```sh
For detailed output, run func with --verbose flag.
[2023-12-19T10:36:30.720Z] Host lock lease acquired by instance ID '0000000000000000000000007053F404'.
[2023-12-19T10:36:31.429Z] Executing 'Functions.Employee_ServiceBus' (Reason='This function was programmatically called via the host APIs.', Id=8e2412bd-7e5f-470a-8c0d-b61f51fef1f0)
[2023-12-19T10:36:31.571Z] Python HTTP trigger function processed a request.
[2023-12-19T10:36:31.571Z] operation ........................AddEmployee
[2023-12-19T10:36:32.350Z] Connection state changed: None -> <ConnectionState.START: 0>
[2023-12-19T10:36:32.829Z] Connection state changed: <ConnectionState.START: 0> -> <ConnectionState.HDR_SENT: 2>
[2023-12-19T10:36:32.830Z] Connection state changed: <ConnectionState.HDR_SENT: 2> -> <ConnectionState.HDR_SENT: 2>
[2023-12-19T10:36:32.834Z] Connection state changed: <ConnectionState.HDR_SENT: 2> -> <ConnectionState.OPEN_PIPE: 4>
[2023-12-19T10:36:32.834Z] Session state changed: <SessionState.UNMAPPED: 0> -> <SessionState.BEGIN_SENT: 1>
[2023-12-19T10:36:32.834Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:36:32.835Z] Management link receiver state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>[2023-12-19T10:36:32.835Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>

[2023-12-19T10:36:32.835Z] Management link sender state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:36:33.085Z] Connection state changed: <ConnectionState.OPEN_PIPE: 4> -> <ConnectionState.OPEN_SENT: 7>
[2023-12-19T10:36:33.136Z] Connection state changed: <ConnectionState.OPEN_SENT: 7> -> <ConnectionState.OPENED: 9>
[2023-12-19T10:36:33.187Z] Session state changed: <SessionState.BEGIN_SENT: 1> -> <SessionState.MAPPED: 3>
[2023-12-19T10:36:33.238Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:36:33.238Z] Management link receiver state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:36:33.289Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:36:33.289Z] Management link sender state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:36:33.657Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:36:33.909Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:36:34.194Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:36:34.194Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:36:34.194Z] Management link receiver state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:36:34.196Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:36:34.198Z] Management link sender state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:36:34.198Z] Session state changed: <SessionState.MAPPED: 3> -> <SessionState.END_SENT: 4>
[2023-12-19T10:36:34.199Z] Connection state changed: <ConnectionState.CLOSE_SENT: 11> -> <ConnectionState.END: 13>
[2023-12-19T10:36:34.199Z] Connection state changed: <ConnectionState.OPENED: 9> -> <ConnectionState.CLOSE_SENT: 11>
[2023-12-19T10:36:34.199Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:36:34.199Z] Management link sender state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:36:34.200Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:36:34.199Z] Session state changed: <SessionState.END_SENT: 4> -> <SessionState.DISCARDING: 6>
[2023-12-19T10:36:34.200Z] Management link receiver state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:36:34.202Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:36:34.318Z] Executing 'Functions.AddEmployeeDetails_ServiceBus' (Reason='(null)', Id=44aced2f-c7a3-4121-a2ab-50803ba303e0)
[2023-12-19T10:36:34.320Z] Trigger Details: MessageId: 7823cb42-9c1b-4002-87ef-a850f25f1728, SequenceNumber: 16, DeliveryCount: 1, EnqueuedTimeUtc: 2023-12-19T10:35:56.1260000+00:00, LockedUntilUtc: 2023-12-19T10:36:56.1410000+00:00, SessionId: (null)
[2023-12-19T10:36:34.359Z] {'EmployeeID': 5555, 'Name': 'Dimple Jain', 'DOB': '15/08/1996', 'Position': 'Analyst'}
[2023-12-19T10:36:34.359Z] Python ServiceBus queue trigger processed message: {"EmployeeID": 5555, "Name": "Dimple Jain", "DOB": "15/08/1996", "Position": "Analyst"}
[2023-12-19T10:36:34.371Z] Python ServiceBus queue trigger processed message.
[2023-12-19T10:36:34.372Z] employee id ................... 5555
[2023-12-19T10:36:34.372Z] employee name ................... Dimple Jain
[2023-12-19T10:36:34.372Z] dob ................... 15/08/1996
[2023-12-19T10:36:34.372Z] position ................... Analyst
[2023-12-19T10:36:34.373Z] logging into Add employee service bus trigger function ...............
[2023-12-19T10:36:34.438Z] Executed 'Functions.AddEmployeeDetails_ServiceBus' (Succeeded, Id=44aced2f-c7a3-4121-a2ab-50803ba303e0, Duration=105ms)
[2023-12-19T10:36:34.833Z] Add Employee Send message is done.
[2023-12-19T10:36:34.900Z] Executed 'Functions.Employee_ServiceBus' (Succeeded, Id=8e2412bd-7e5f-470a-8c0d-b61f51fef1f0, Duration=3567ms)
```

CSV file 
```
EmployeeID,Name,DOB,Position
3450,Foram Jivani,09/12/1991,MLE
3485,Abc XYC,01/01/1990,Sr MLE
3330,Def XYC,01/02/1996,Analyst
3200,ERF XYC,06/08/1992,MLE
2009,Abc XYC,01/01/1990,Sr MLE
2008,Def XYC,01/02/1996,Analyst
2001,ERF XYC,06/08/1992,MLE
2010,Abc XYC,01/01/1990,Sr MLE
1010,Def XYC,01/02/1996,Analyst
1100,ERF XYC,06/08/1992,MLE
5200,Abc XYC,01/01/1990,Sr MLE
2586,Def XYC,01/02/1996,Analyst
9874,ERF XYC,06/08/1992,MLE
1111,ERF XYC,06/08/1992,MLE
5598,Abc XYC,01/01/1990,Sr MLE
7845,Def XYC,01/02/1996,Analyst
9854,ERF XYC,06/08/1992,MLE
5555,Dimple Jain,15/08/1996,Analyst
```


Send `POST` request to  
`http://localhost:7071/api/Employee_ServiceBus?Operation=DeleteEmployee`
with following json body
```
{
    "EmployeeID": 5555
}
```

```sh
[2023-12-19T10:37:49.227Z] operation ........................DeleteEmployee
[2023-12-19T10:37:49.227Z] Python HTTP trigger function processed a request.
[2023-12-19T10:37:50.076Z] Connection state changed: None -> <ConnectionState.START: 0>
[2023-12-19T10:37:50.583Z] Connection state changed: <ConnectionState.START: 0> -> <ConnectionState.HDR_SENT: 2>
[2023-12-19T10:37:50.584Z] Connection state changed: <ConnectionState.HDR_SENT: 2> -> <ConnectionState.HDR_SENT: 2>
[2023-12-19T10:37:50.587Z] Connection state changed: <ConnectionState.HDR_SENT: 2> -> <ConnectionState.OPEN_PIPE: 4>
[2023-12-19T10:37:50.587Z] Session state changed: <SessionState.UNMAPPED: 0> -> <SessionState.BEGIN_SENT: 1>
[2023-12-19T10:37:50.587Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:37:50.588Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:37:50.588Z] Management link sender state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:37:50.588Z] Management link receiver state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:37:50.877Z] Connection state changed: <ConnectionState.OPEN_PIPE: 4> -> <ConnectionState.OPEN_SENT: 7>
[2023-12-19T10:37:50.928Z] Connection state changed: <ConnectionState.OPEN_SENT: 7> -> <ConnectionState.OPENED: 9>
[2023-12-19T10:37:50.979Z] Session state changed: <SessionState.BEGIN_SENT: 1> -> <SessionState.MAPPED: 3>
[2023-12-19T10:37:51.030Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>[2023-12-19T10:37:51.030Z] Management link receiver state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>

[2023-12-19T10:37:51.081Z] Management link sender state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:37:51.081Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:37:51.567Z] Link state changed: <LinkState.DETACHED: 0> -> <LinkState.ATTACH_SENT: 1>
[2023-12-19T10:37:51.819Z] Link state changed: <LinkState.ATTACH_SENT: 1> -> <LinkState.ATTACHED: 3>
[2023-12-19T10:37:52.089Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:37:52.091Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:37:52.092Z] Management link receiver state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:37:52.092Z] Link state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:37:52.092Z] Management link sender state changed: <LinkState.ATTACHED: 3> -> <LinkState.DETACH_SENT: 4>
[2023-12-19T10:37:52.093Z] Session state changed: <SessionState.MAPPED: 3> -> <SessionState.END_SENT: 4>
[2023-12-19T10:37:52.093Z] Connection state changed: <ConnectionState.OPENED: 9> -> <ConnectionState.CLOSE_SENT: 11>
[2023-12-19T10:37:52.093Z] Connection state changed: <ConnectionState.CLOSE_SENT: 11> -> <ConnectionState.END: 13>
[2023-12-19T10:37:52.094Z] Session state changed: <SessionState.END_SENT: 4> -> <SessionState.DISCARDING: 6>
[2023-12-19T10:37:52.094Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:37:52.094Z] Management link sender state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:37:52.094Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:37:52.094Z] Management link receiver state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:37:52.094Z] Link state changed: <LinkState.DETACH_SENT: 4> -> <LinkState.DETACHED: 0>
[2023-12-19T10:37:52.221Z] Executing 'Functions.DeleteEmployeeDetails_ServiceBus' (Reason='(null)', Id=3e1ebb08-b355-4f98-99e5-3b19f6ce41de)
[2023-12-19T10:37:52.221Z] Trigger Details: MessageId: 24fe5ae1-9338-43ab-bb84-432c76bf351a, SequenceNumber: 17, DeliveryCount: 1, EnqueuedTimeUtc: 2023-12-19T10:37:14.1270000+00:00, LockedUntilUtc: 2023-12-19T10:38:14.1420000+00:00, SessionId: (null)
[2023-12-19T10:37:52.226Z] Python ServiceBus queue trigger processed message: 5555
[2023-12-19T10:37:52.226Z] EmployeeID: 5555
[2023-12-19T10:37:52.246Z] Python ServiceBus queue trigger processed message for EmployeeID: 5555
[2023-12-19T10:37:52.247Z] logging from Delete service bus trigger ......................
[2023-12-19T10:37:52.247Z] Executed 'Functions.DeleteEmployeeDetails_ServiceBus' (Succeeded, Id=3e1ebb08-b355-4f98-99e5-3b19f6ce41de, Duration=27ms)
[2023-12-19T10:37:52.247Z] deleted data ..................... {'EmployeeID': '5555', 'Name': 'Dimple Jain', 'DOB': '15/08/1996', 'Position': 'Analyst'}
[2023-12-19T10:37:52.587Z] Delete Employee Send message is done.
[2023-12-19T10:37:52.588Z] Executed 'Functions.Employee_ServiceBus' (Succeeded, Id=38a357d2-1ebd-404e-9b45-0a062e978bdb, Duration=3374ms)
```

CSV file 
```
EmployeeID,Name,DOB,Position
3450,Foram Jivani,09/12/1991,MLE
3485,Abc XYC,01/01/1990,Sr MLE
3330,Def XYC,01/02/1996,Analyst
3200,ERF XYC,06/08/1992,MLE
2009,Abc XYC,01/01/1990,Sr MLE
2008,Def XYC,01/02/1996,Analyst
2001,ERF XYC,06/08/1992,MLE
2010,Abc XYC,01/01/1990,Sr MLE
1010,Def XYC,01/02/1996,Analyst
1100,ERF XYC,06/08/1992,MLE
5200,Abc XYC,01/01/1990,Sr MLE
2586,Def XYC,01/02/1996,Analyst
9874,ERF XYC,06/08/1992,MLE
1111,ERF XYC,06/08/1992,MLE
5598,Abc XYC,01/01/1990,Sr MLE
7845,Def XYC,01/02/1996,Analyst
9854,ERF XYC,06/08/1992,MLE
```

