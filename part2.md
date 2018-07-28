## Setup - RIAK not available
* RIAK version 2.2.3 installed via official Ubuntu repository
```
$ export RIAK_HOST="http://localhost:8098"
$ curl -XPUT $RIAK_HOST/search/index/newssearch                                                                         ~/Documents/Job Interviews/nhs/solutions/nhsTest
<HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD><BODY><H1>Not Found</H1>The requested document was not found on this server.<P><HR><ADDRESS>mochiweb+webmachine web server</ADDRESS></BODY></HTML>%
```

checkup on google shows it might be problem in installation

so the following listing is based only on RIAK's documentation

## Common query caching

### Create search index
```
$ curl -XPUT $RIAK_HOST/search/index/newssearch
```
### Create bucket type
```
$ riak-admin bucket-type create queries '{"props":{"search_index":"newssearch"}}'
$ riak-admin bucket-type activate queries
```
### Add top 5 queries

```
$ curl -XPUT $RIAK_HOST/types/queries/buckets/orquery/keys/carequalitycommision \
     -H 'Content-Type: application/json' \
     -d '{"query_s":"Care Quality Commission", "type_s":"OR", "result_s":"0,1,2,3,4,5,6"}'

$ curl -XPUT $RIAK_HOST/types/queries/buckets/orquery/keys/september2004\
     -H 'Content-Type: application/json' \
     -d '{"query_s":"September 2004", "type_s":"OR", "result_s":"9"}'

$ curl -XPUT $RIAK_HOST/types/queries/buckets/orquery/keys/generalpopulationgenerally\
     -H 'Content-Type: application/json' \
     -d '{"query_s":"general population generally", "type_s":"OR", "result_s":"6,8"}'

$ curl -XPUT $RIAK_HOST/types/queries/buckets/andquery/keys/carequalitycommissionadmission\
     -H 'Content-Type: application/json' \
     -d '{"query_s":"Care Quality Commission admission", "type_s":"AND", "result_s":"1"}'

$ curl -XPUT $RIAK_HOST/types/queries/buckets/andquery/keys/generalpopulationalzheimer\
     -H 'Content-Type: application/json' \
     -d '{"query_s":"general population Alzheimer", "type_s":"AND", "result_s":"6"}'
```

### Query
```
$ curl "$RIAK_HOST/search/query/newssearch?wt=json&q=query_s:Care%20Quality%20Commission" | jsonpp

{
  "numFound": 1,
  "start": 0,
  "maxScore": 1.0,
  "docs": [
    {
      "query_s": "Care Quality Commission",
      "type_s": "OR",
      "result_s": "0,1,2,3,4,5,6",
      "_yz_id": "default_orquery_carequalitycommision_37",
      "_yz_rk": "carequalitycommisio",
      "_yz_rt": "default",
      "_yz_rb": "orquery"
    }
  ]
}
```

## Monthly indexes

### Insert indexes
Current insert requests make the assumption that there is one news per date.
If this is not the case, hour, minute and second could be included or
more complex enumeration if two or more news collide to the second.

```
$ curl -XPUT $RIAK_HOST/buckets/hscicNews/keys/result:0\
     -H "x-riak-index-date: 2013-06-05"
     -H 'Content-Type: application/json' \
     -d '{"content_s":"June 5 , 2013 : The majority of carers say they are extremely..."}'

$ curl -XPUT $RIAK_HOST/buckets/hscicNews/keys/result:1\
     -H "x-riak-index-date: 2013-07-09"
     -H 'Content-Type: application/json' \
     -d '{"content_s":"July 9 , 2013 : The HSCIC has extended the consultation..."}'

```

### Query news by month/year
```
curl $RIAK_HOST/types/indexes/buckets/hscicNews/index/date/2013-06-01/2013-06-31??return_terms=true

```
