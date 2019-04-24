function SoundIcon(props) {
    var dir = props.dir;
    var ext = props.imgExt;
    var imgsrc = `bin/sounds/${dir}/img.${ext}`

    var playSound = props.playSound;

    return (
        <div className="SoundIcon" onClick={playSound}>
            <img src={imgsrc} height="100" />
            <span>{dir}</span>
        </div>
    )

}

function Soundboard(props) {
    var icons = props.dirList.map(function(dir) {
        return <SoundIcon dir={dir.key} imgExt={dir.imgExt} playSound={() => playSound(dir.key)} key={dir.key} />
    })

    return (
        <div className="Soundboard">
            {icons}
        </div>
    )
}

function getSounds() {
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: "/get_sounds",
            dataType: "json",
            type: "GET"
        }).done(resp => resolve(resp));
    })
}

function playSound(sound) {
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: "/play_sound",
            dataType: "json",
            type: "GET",
            data: {sound: sound}
        }).done(resp => resolve(resp));
    })
}

getSounds().then(resp => ReactDOM.render(<Soundboard dirList={resp}/>, document.getElementById("main")))