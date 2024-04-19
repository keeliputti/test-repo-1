

Scenario 1: In case of library upgrades/a new lib added to dzparts?:
Say the client has installed dzc 10 days ago.
Update was made 4 days ago.

Impact:
Because he has a missing library which was installed in dzparts, he would get Error - which he would have to install? 
or
upgrade to latest dzpy client, because the latest of dzparts only gets installed when you install dzpy again.



Scenario 2: Pydantic validation changes in dzparts
Say the client has installed dzc 10 days ago.
Update was made 4 days ago.

Impact:
Client will set configs according to the older Model - His Client Validation passes
Server validation would fail!! (because server has latest version)

(e.g. say client pydantic rule says dz-captains-group > 3 charcters.
However server Pydantic rules says - dz-captains-group < 3 characters

Client confused!!)



Would we be adding adding Pydantic validations in all clients? - dzjava, dzr, dzq?

Yes: 
Scenario 3: changes required in Pydantic rules!

Impact:
Would we have to update all clients for any change in pydantic?
Do all languages support Pydantic?


No:
Then why in dzpy? 



Answer: No. Validations for other clients would happen at server side only
