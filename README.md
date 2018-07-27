# newssearch
Implements search routines and perform queries on a set of documents defined as
follows:

```
June 5 , 2013 : The majority of carers say they are extremely , very or quite satisfied with the support and services they and the person they care for receive , according to a survey published today . Of the 57 , 800 carers who took part in the survey , 36 per cent reported that they were either extremely or very satisfied with the support and services they and the person they care for received , with 29 per cent said they were quite satisfied . However , 5 per cent reported they were quite dissatisfied and 4 per cent stated they were either very or extremely dissatisfied . 11 per cent reported that they were neither satisfied nor dissatisfied , and 16 per cent reported that they hadn ' t received any support or services from Social Services in the last 12 months . These provisional findings are contained in the Personal Social Services Survey of Adult Carers in England 2012 - 13 published today by the Health and Social Care Information Centre ( HSCIC ) . The survey is of carers aged 18 and caring for someone aged 18 or over who receives services funded wholly or in part by social services . The biennial survey examines how far carers are able to have a balanced life alongside their caring role and whether services provided by local authorities and other organisations are supporting carers well .
July 9 , 2013 : The HSCIC has extended the consultation period on a draft list of conditions to be included in a proposed ' Present on Admission flag ' . There are a number of conditions that , whilst preventable , can be acquired in hospitals and have an adverse effect on a patients morbidity and / or involve substantial financial cost to the hospital . Analysis of these conditions is currently difficult as it is not always known whether a condition has been acquired during the patients stay or was present at the time of admission to the hospital . If introduced a Present on admission flag could enable identification of conditions that were acquired by patients during their stay and those that existed prior to admission . This would enable better analysis of these conditions , helping to attribute the condition to the appropriate timeframe and in turn identify good practice . The Health and Social Care Information Centre ( HSCIC ) is working with key stakeholders , including the Academy of Medical Royal Colleges ( AoMRC ) , Royal College of Nursing ( RCN ) and Care Quality Commission ( CQC ) to define a candidate list of Present on Admission conditions and associated guidance . We are keen to hear from stakeholders , particularly clinicians and healthcare specialists . The consultation has now been extended until Sunday 28 July to enable as wide a range of stakeholders to respond as possible .
June 19 , 2013 : New figures from the Health and Social Care Information Centre ( HSCIC ) show in 2012 - 13 ( 2 ) almost two million patients were treated at the scene ( 3 ) by ambulance services without needing onward transportation , a 10 per cent rise on last year ' s figure ( 1 . 81 million ) . Of these patients more than one in three ( 34 . 2 per cent ) had been assessed by the call handler as falling into Category A , which meant their condition was potentially life threatening . Today ' s Ambulance Services , England : 2012 - 13 report shows control rooms received 9 . 08 million emergency calls in 2012 - 132 , a rise of more than half a million ( 6 . 9 per cent ) on 2011 - 12 and one in three of these was recorded as Category A ( 32 . 5 per cent , or 2 . 95 million ) .
June 13 , 2013 : Almost one in five women who gave birth in the North East in 2012 - 13 classed themselves as a smoker when they had their baby , new figures show . Nearly 5 , 700 women ( 19 . 7 per cent of 28 , 920 ) said they still smoked according to today ' s Health and Social Care Information Centre ( HSCIC ) report , which also shows this prevalence has been highest in the North East for the last six years . London had the lowest prevalence in 2012 - 13 at about one in 17 ( 5 . 7 per cent , or 7 , 000 out of 122 , 320 ) and also had the lowest prevalence in each of the last six years . Blackpool Primary Care Trust ( PCT ) had the highest prevalence of all 147 PCTS who returned validated data with almost one in three women smoking during pregnancy ( 30 . 8 per cent , or 520 out of 1 , 700 ) . Westminster PCT had the lowest rate at about one in 43 ( 2 . 3 per cent , or 54 out of 2 , 380 ) .
June 5 , 2013 : The majority of carers say they are extremely , very or quite satisfied with the support and services they and the person they care for receive , according to a survey published today . Of the 57 , 800 carers who took part in the survey , 36 per cent reported that they were either extremely or very satisfied with the support and services they and the person they care for received , with 29 per cent said they were quite satisfied . However , 5 per cent reported they were quite dissatisfied and 4 per cent stated they were either very or extremely dissatisfied . 11 per cent reported that they were neither satisfied nor dissatisfied , and 16 per cent reported that they hadn ' t received any support or services from Social Services in the last 12 months3 . These provisional findings are contained in the Personal Social Services Survey of Adult Carers in England 2012 - 13 published today by the Health and Social Care Information Centre ( HSCIC ) . The survey is of carers aged 18 and caring for someone aged 18 or over who receives services funded wholly or in part by social services . The biennial survey examines how far carers are able to have a balanced life alongside their caring role and whether services provided by local authorities and other organisations are supporting carers well .
April 15 , 2013 Thousands of GP practices around the country that have benefited from having their clinical IT systems provided under GP Systems of Choice ( GPSoC ) will now enjoy continuity of provision as a result of an extension to the current GPSoC arrangements . GPSoC has successfully delivered a flexible mechanism for contracting for GP clinical IT systems in GP practices since 2007 and 81 per cent of practices currently use a system provided through the framework . GP clinical IT systems are key to collecting and sharing patient data to support clinical care . They also provide access to national services including Choose and Book , the Electronic Prescription Service , Summary Care Records and GP2GP electronic transfer of patient records . The extension was arranged by the GPSoC team , now part of the Health and Social Care Information Centre ( HSCIC ) . As well as being the trusted source of data and information relating to health and care , HSCIC supports the delivery of IT infrastructure , information systems and standards to ensure information flows efficiently and securely across the health and social care system to improve patient outcomes . The HSCIC was established as an Executive Non - Departmental Public Body on 1st April . In addition to working on the extension , the GPSoC team has also been consulting widely with both GP representatives and the supplier community on new contracting arrangements to support the delivery of GP clinical IT systems in the future . NHS England is also heavily involved in this work , as the new sponsor of GPSoC .
```

### Prerequisites

Python 2.7.x installed on the PC (Windows 7 or Ubuntu >= 12.04)

### Installing

1) download the git repository https://github.com/dmanev/nhsTest.git
2) cd nhsTest

### Running

```
# python ns.py -o "Care Quality  Commission"                                                                                 
0, 1, 2, 3, 4, 5, 6

OR

# ./ns.py -o "Care Quality  Commission"                                                                                 
0, 1, 2, 3, 4, 5, 6

(make sure ns.py is with executable flag for Linux/Unix environment )
```


### Running the test
```
# python -m unittest test.test_newssearch                                                                              
.keyword not found: 'admission4'
keyword not found: 'Alzheimer1'
...
----------------------------------------------------------------------
Ran 4 tests in 0.019s

OK

```
