package main

import (
    "context"
    "fmt"
    "github.com/aws/aws-lambda-go/events"
    openTelemetryTrace "github.com/StackVista/stackstate-agent/pkg/trace/pb/open-telemetry/trace/v1"
    runtime "github.com/aws/aws-lambda-go/lambda"
    "github.com/gogo/protobuf/proto"
)

func main() {
    runtime.Start(Handler)
}

func Handler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
    traceData := &openTelemetryTrace.TracesData{}
    if err := proto.Unmarshal([]byte(request.Body), traceData); err != nil {
        fmt.Printf("%v", err)
    }
    fmt.Printf("%v", traceData)

    traceData2 := &openTelemetryTrace.ResourceSpans{}
    if err := proto.Unmarshal([]byte(request.Body), traceData2); err != nil {
        fmt.Printf("%v", err)
    }
    fmt.Printf("%v", traceData2)

    traceData3 := &openTelemetryTrace.InstrumentationLibrarySpans{}
    if err := proto.Unmarshal([]byte(request.Body), traceData3); err != nil {
        fmt.Printf("%v\n", err)
    }
    fmt.Printf("%v\n\n", traceData3)

    traceData4 := &openTelemetryTrace.Span{}
    if err := proto.Unmarshal([]byte(request.Body), traceData4); err != nil {
        fmt.Printf("%v\n", err)
    }
    fmt.Printf("%v\n\n", traceData4)

    traceData5 := &openTelemetryTrace.Span_Event{}
    if err := proto.Unmarshal([]byte(request.Body), traceData5); err != nil {
        fmt.Printf("%v\n", err)
    }
    fmt.Printf("%v\n\n", traceData5)

    traceData6 := &openTelemetryTrace.Span_Link{}
    if err := proto.Unmarshal([]byte(request.Body), traceData6); err != nil {
        fmt.Printf("%v\n", err)
    }
    fmt.Printf("%v\n\n", traceData6)

    traceData7 := &openTelemetryTrace.Status{}
    if err := proto.Unmarshal([]byte(request.Body), traceData7); err != nil {
        fmt.Printf("%v\n", err)
    }
    fmt.Printf("%v\n\n", traceData7)

    // fmt.Printf("Processing request data for request %s.\n", request.RequestContext.RequestID)
    // fmt.Printf("Body size = %d.\n", len(request.Body))

    // fmt.Println("Headers:")
    // for key, value := range request.Headers {
    //     fmt.Printf("    %s: %s\n", key, value)
    // }

    return events.APIGatewayProxyResponse{Body: request.Body, StatusCode: 200}, nil
}