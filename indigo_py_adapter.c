// Package up a few functions for easier CFFI interface
//

#include "indigo_bus.h"
#include "indigo_client.h"
#include "indigo_xml.h"
#include <string.h>


// Create and attach an indigo_client (see indigo_bus.h) with Python callbacks

static indigo_client client;

indigo_client *indigo_build_client(char *client_name, indigo_result (*attach_cb)(indigo_client *client),
				   indigo_result (*define_property_cb)(indigo_client *client, indigo_device *device, indigo_property *property, const char *message),
				   indigo_result (*update_property_cb)(indigo_client *client, indigo_device *device, indigo_property *property, const char *message),
				   indigo_result (*delete_property_cb)(indigo_client *client, indigo_device *device, indigo_property *property, const char *message),
				   indigo_result (*send_message_cb)(indigo_client *client, indigo_device *device, const char *message),
				   indigo_result (*detach_cb)(indigo_client *client)
				   )
{

  strncpy(client.name, client_name, INDIGO_NAME_SIZE);
  client.is_remote = false;
  client.client_context = NULL;
  client.last_result = INDIGO_OK;
  client.version = INDIGO_VERSION_CURRENT;
  client.enable_blob_mode_records = NULL;
  client.attach = attach_cb;
  client.define_property = define_property_cb;
  client.update_property = update_property_cb;
  client.delete_property = delete_property_cb;
  client.detach = detach_cb;
  
  indigo_attach_client(&client);
  return &client;
}
