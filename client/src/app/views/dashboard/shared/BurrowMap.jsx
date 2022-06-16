import React, { useState, useEffect } from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"

const MyMapComponent = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `400px` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }),
  withScriptjs,
  withGoogleMap
)((props) =>
  <GoogleMap
    defaultZoom={8}
    defaultCenter={{ lat: 26.6451, lng: -81.9866 }}
  >
    {props.isMarkerShown && <Marker position={{ lat: 26.6451, lng: -81.9866 }} onClick={props.onMarkerClick} />}
  </GoogleMap>
)

const BurrowMap = () => {
  const [isMarkerShown, setIsMarkerShown] = useState(false);

  useEffect(() => {
    delayedShowMarker();
  }, []);

  const delayedShowMarker = () => {
    setTimeout(() => {
      setIsMarkerShown(true);
    }, 3000)
  };

  const handleMarkerClick = () => {
    setIsMarkerShown(true);
    delayedShowMarker();
  };

    return (
      <MyMapComponent
        isMarkerShown={isMarkerShown}
        onMarkerClick={handleMarkerClick}
      />
    )
}

export default BurrowMap;
