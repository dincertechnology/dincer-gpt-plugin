# Dincer Logistics ChatGPT Plugin Privacy Policy

**Effective date:** July 30, 2026

This connector-specific notice supplements the official
[Dincer Logistics Privacy and Cookie Policy](https://dincerlogistics.com/gizlilik-ve-cerez-politikasi/).
The official company policy is the primary privacy policy for the OpenAI
Plugin Directory listing.

Dincer Logistics operates the Dincer Logistics plugin for ChatGPT and Codex. This
policy explains how information is handled when you register for and use the
connector.

## Information we process

- Questions sent through the connector and the matching workbook content are
  processed to return the requested answer.
- Your email address, connector account, and authentication records are processed
  by Amazon Cognito to register you and control access.
- Technical records such as request time, status, error details, and service
  diagnostics may be stored in Amazon CloudWatch Logs.

## How we use information

Information is used only to authenticate users, provide the connector, protect the service,
troubleshoot failures, and meet legal or security
obligations. We do not sell personal information or use connector data for
advertising.

## Service providers and data flow

The connector uses Amazon Web Services, including Cognito, API Gateway, Lambda,
S3, and CloudWatch. ChatGPT or Codex sends tool requests to the connector
and receives tool results, so OpenAI also processes that information under its
own terms and privacy policy. Source workbooks remain in Dincer Logistics'
AWS environment and are not stored in the public plugin repository.

## Retention and security

CloudWatch technical logs are retained for 30 days. Cognito account data is
retained while the connector account remains active and may be deleted upon a
valid request, subject to legal obligations. Connector queries and
workbook results are processed transiently by Lambda; a short-lived in-memory
cache may exist only while a Lambda execution environment remains active.
Access to source data is read-only and limited to the approved AWS resources.
Traffic uses HTTPS, and access is protected with OAuth 2.0 through Amazon Cognito.

## Your choices

You may disconnect the plugin in ChatGPT or Codex at any time. To request access,
correction, or deletion of connector account information, contact
[info@dincerlojistik.com](mailto:info@dincerlojistik.com).

## Changes

We may update this policy as the connector or legal requirements change. The
effective date above will be updated when changes are published.

## Contact

Dincer Logistics  
[https://dincerlogistics.com/](https://dincerlogistics.com/)  
[info@dincerlojistik.com](mailto:info@dincerlojistik.com)
