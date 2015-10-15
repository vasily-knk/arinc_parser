
fields_runway = [
    6,    # Airport_ICAO_Identifier
    46,   # Runway_Identifier
    57,   # Runway_Length
    109,  # Runway_Width
    36,   # Runway_Latitude
    37,   # Runway_Longitude
    58,   # Runway_Magnetic_Bearing
]

fields_sid_star_approach = [
    6,   # airport_identifier
    30,  # altitude
    30,  # altitude_2
    29,  # altitude_description
    13,  # fix_identifier
    14,  # icao_code_2
    14,  # icao_code_3
    26,  # magnetic_course
    21,  # path_and_termination
    23,  # recommended_navaid
    27,  # route_distance_or_time
    7,   # route_type
    12,  # sequence_number
    9, 10, # sid_star_approach_identifier
    5,   # subsection_code
    11,  # transitition_indicator
    20,  # turn_direction
    17,  # waypoint_description_code
]

fields_controlled_airspace = [
    118,  # Boundary_Via,
    36,   # Latitude,
    37,   # Longitude,
    36,   # Arc_Origin_Latitude,
    37,   # Arc_Origin_Longitude,
    119,  # Arc_Distance,
    120,  # Arc_Bearing,
    121,  # Lower_Level,
    121,  # Upper_Level,
    216,  # Controlled_Airspace_Name,
    213,  # Airspace_Type
]

fields_fir_uir = [
    116,  # fir_uir_identifier
    36,   # fir_uir_latitude
    37,   # fir_uir_longitude
]

fields_enroute_airways = [
    3,   # ea.area_code
    13,  # ea.fix_identifier
    14,  # ea.icao_code
    8,   # ea.route_identifier
    7,   # ea.route_type
    12,  # ea.sequence_number
    17,  # ea.waypoint_description_code
]

fields_waypoint = [
    13,  # wp.waypoint_identifier
    36,  # wp.waypoint_latitude
    37,  # wp.waypoint_longitude
]

fields_ndb_navaid = [
    14,   # nn.icao_code_2
    33,   # nn.ndb_identifier
    36,   # nn.ndb_latitude
    37,   # nn.ndb_longitude
]

fields_vhf_navaid = [
    36,  # vn.dme_latitude
    37,  # vn.dme_longitude
    36,  # vn.icao_code_2
    37,  # vn.section_code
    33,  # vn.vor_identifier
    36,  # vn.vor_latitude
    37,  # vn.vor_longitude
]

needed_fields = set(fields_runway) \
    | set(fields_sid_star_approach) \
    | set(fields_controlled_airspace) \
    | set(fields_fir_uir) \
    | set(fields_enroute_airways) \
    | set(fields_waypoint) \
    | set(fields_ndb_navaid) \
    | set(fields_vhf_navaid)

print needed_fields