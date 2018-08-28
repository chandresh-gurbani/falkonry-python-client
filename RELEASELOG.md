# Release Log

### 2.2.1
* Support for offset in live monitoring Refer to release note - https://github.com/Falkonry/falkonry-python-client/releases/tag/2.2.1

### 2.2.0
* Support for turn on/off live monitoring for a specific assessment. Refer to release note - https://github.com/Falkonry/falkonry-python-client/releases/tag/2.2.0

### 2.1.1
* Bug fix for keywordIdentifier not getting picked up during fact data upload.

### 2.1.0
* Renamed tagIdentifier to keywordIdentifier
* Renamed additionalTag to additionalKeyword

### 2.0.0
* Supports python 3. Refer to release note - https://github.com/Falkonry/falkonry-python-client/releases/tag/2.0.0

### 1.1.0
* API changes for batched window datastream

### 1.0.5
* Support for new narrow formatted data

### 1.0.4
* Support for custom column identifiers for fact API

### 1.0.3
* Support for time precision upto microseconds

### 1.0.2
* Minor bug fix

### 1.0.1
* Support for downloading input data and fact data.

### 1.0.0
* [Updated] New API integration. Refer to readme.

### 0.2.9
* Simplifying output streaming.

### 0.2.8
* Supports assessment output streaming.

### 0.2.6
* Auth token update: Just copy/paste auth token from Falkonry Service UI.

### 0.2.5
* Terminology changes. Refer to release note - https://github.com/Falkonry/falkonry-python-client/releases/tag/0.2.5

### 0.2.4
* Support for narrow format data

### 0.2.3
* API changes for eventbuffer and pipeline creation. Refer to release note - https://github.com/Falkonry/falkonry-python-client/releases/tag/0.2.3

### 0.2.2
* Support to add eventType for signal
* Support to add facts data

### 0.2.1
* Bug fixes and readme update

### 0.2.0
* Create Eventbuffer
* Retrieve Eventbuffers
* Create Pipeline
* Retrieve Pipelines
* Add data to Eventbuffer (csv/json, stream)
* Retrieve output of Pipeline
* Create/update/delete subscription for Eventbuffer
* Create/update/delete publication for Pipeline

### 0.1.5
* Support to create Eventbuffer
* Support to create Pipeline from Eventbuffer
* Support to add input csv or json data / stream to a Eventbuffer
* Support to create subscription for Evenbuffer data ingestion
* Support to create publication for Pipeline
* Change in data ingestion and pipeline creation APIs

### 0.1.4
* Support to create Pipeline
* Support to get list of Pipelines
* Support to add input json data / stream to a Pipeline
* Support to get output of a Pipeline